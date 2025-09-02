Installation Guide
==================

System Requirements
-------------------

- PHP 7.4 atau lebih tinggi
- MySQL 5.7+ atau MariaDB 10.3+
- Apache/Nginx dengan mod_rewrite
- Composer

Step-by-Step Installation
-------------------------

1. **Clone Repository**:

   .. code-block:: bash

      git clone https://github.com/username/your-project.git
      cd your-project

2. **Install Dependencies**:

   .. code-block:: bash

      composer install

3. **Database Setup**:

   .. code-block:: bash

      # Import database schema
      mysql -u username -p database_name < database/schema.sql

4. **Configuration**:

   Edit file ``application/config/config.php`` dan ``database.php``

5. **Folder Permissions**:

   .. code-block:: bash

      chmod -R 755 application/cache
      chmod -R 755 application/logs
      chmod -R 755 uploads

Environment Setup
-----------------

.. code-block:: bash

   # Development environment
   cp env.example .env
   # Edit environment variables