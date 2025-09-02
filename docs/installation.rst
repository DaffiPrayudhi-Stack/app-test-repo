Installation Guide
==================

Prerequisites
-------------
- PHP 7.4 atau lebih tinggi
- MySQL 5.7+
- Composer
- Apache/Nginx

Step-by-Step Installation
-------------------------

1. Clone Repository
   .. code-block:: bash

      git clone https://github.com/username/your-project.git
      cd your-project

2. Install Dependencies
   .. code-block:: bash

      composer install

3. Database Setup
   .. code-block:: bash

      # Import database schema
      mysql -u username -p database_name < database/schema.sql

4. Configuration
   .. code-block:: bash

      # Copy environment file
      cp .env.example .env
      # Edit configuration
      nano .env

Environment Variables
--------------------
.. list-table::
   :header-rows: 1

   * - Variable
     - Description
     - Example
   * - ``CI_ENV``
     - Environment type
     - development/production
   * - ``database.default.hostname``
     - Database host
     - localhost
   * - ``database.default.database``
     - Database name
     - myapp_db