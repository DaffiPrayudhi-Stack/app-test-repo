Controllers Reference
=====================

Base Controller
---------------

.. code-block:: php
   :linenos:
   
   <?php
   defined('BASEPATH') OR exit('No direct script access allowed');
   
   class Base_Controller extends CI_Controller {
       
       public function __construct() {
           parent::__construct();
           $this->load->library('session');
           $this->load->helper('url');
       }
       
       protected function _render($view, $data = []) {
           $this->load->view('templates/header', $data);
           $this->load->view($view, $data);
           $this->load->view('templates/footer', $data);
       }
   }

User Controller
---------------

.. php:class:: User_Controller

   Controller untuk manajemen user

   .. php:method:: index()
      
      Menampilkan daftar user
      
      **Route:** ``GET /users``
      
      **Returns:** View users/list

   .. php:method:: create()
      
      Form create user
      
      **Route:** ``GET /users/create``

   .. php:method:: store()
      
      Simpan user baru
      
      **Route:** ``POST /users``