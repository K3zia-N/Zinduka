#!/usr/bin/env python3
"""
Database connection test script for Zinduka Flask app
This script tests the database connection and table structure
"""

from db import get_db_connection
import pymysql

def test_connection():
    """Test basic database connection"""
    try:
        conn = get_db_connection()
        print("[SUCCESS] Database connection successful!")
        
        cursor = conn.cursor()
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"[SUCCESS] MySQL version: {version[0]}")
        
        cursor.execute("SELECT DATABASE()")
        db_name = cursor.fetchone()
        print(f"[SUCCESS] Connected to database: {db_name[0]}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Database connection failed: {e}")
        return False

def check_tables():
    """Check if required tables exist"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Check for required tables
        required_tables = ['cases', 'survivorstories', 'donation']
        
        cursor.execute("SHOW TABLES")
        existing_tables = [table[0] for table in cursor.fetchall()]
        
        print(f"[INFO] Existing tables: {existing_tables}")
        
        for table in required_tables:
            if table in existing_tables:
                print(f"[SUCCESS] Table '{table}' exists")
                
                # Show table structure
                cursor.execute(f"DESCRIBE {table}")
                columns = cursor.fetchall()
                print(f"   Columns in {table}:")
                for col in columns:
                    print(f"     - {col[0]} ({col[1]})")
            else:
                print(f"[ERROR] Table '{table}' missing")
        
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Error checking tables: {e}")
        return False

def create_tables():
    """Create required tables if they don't exist"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Create cases table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cases (
                id INT AUTO_INCREMENT PRIMARY KEY,
                userName VARCHAR(255) NOT NULL,
                contactNumber VARCHAR(20) NOT NULL,
                address TEXT NOT NULL,
                email VARCHAR(255) NOT NULL,
                country VARCHAR(100) NOT NULL,
                city VARCHAR(100) NOT NULL,
                caseType VARCHAR(100) NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create survivorstories table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS survivorstories (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                yourStory TEXT NOT NULL,
                digitalSignature VARCHAR(255) NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Create donation table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS donation (
                id INT AUTO_INCREMENT PRIMARY KEY,
                donationAmount DECIMAL(10,2) NOT NULL,
                fullName VARCHAR(255) NOT NULL,
                emailAddress VARCHAR(255) NOT NULL,
                paymentMethod VARCHAR(50) NOT NULL,
                message TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        conn.commit()
        print("[SUCCESS] All required tables created successfully!")
        
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Error creating tables: {e}")
        return False

def test_insert():
    """Test inserting sample data"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Test case insertion
        cursor.execute("""
            INSERT INTO cases (userName, contactNumber, address, email, country, city, caseType, message)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, ("Test User", "0700000000", "Test Address", "test@example.com", "Kenya", "Nairobi", "harassment", "Test message"))
        
        print("[SUCCESS] Test case inserted successfully!")
        
        # Test story insertion
        cursor.execute("""
            INSERT INTO survivorstories (name, yourStory, digitalSignature)
            VALUES (%s, %s, %s)
        """, ("Test Survivor", "This is a test story", "Test Signature"))
        
        print("[SUCCESS] Test story inserted successfully!")
        
        # Test donation insertion
        cursor.execute("""
            INSERT INTO donation (donationAmount, fullName, emailAddress, paymentMethod, message)
            VALUES (%s, %s, %s, %s, %s)
        """, (100.00, "Test Donor", "donor@example.com", "mpesa", "Test donation"))
        
        print("[SUCCESS] Test donation inserted successfully!")
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"[ERROR] Error inserting test data: {e}")
        return False

if __name__ == "__main__":
    print("Testing Zinduka Database Connection...")
    print("=" * 50)
    
    # Test connection
    if not test_connection():
        print("\nDatabase connection failed. Please check your XAMPP MySQL server.")
        exit(1)
    
    print("\nChecking table structure...")
    check_tables()
    
    print("\nCreating missing tables...")
    create_tables()
    
    print("\nTesting data insertion...")
    test_insert()
    
    print("\nDatabase test completed successfully!")
    print("Your Flask app should now be able to save data to MySQL.")
