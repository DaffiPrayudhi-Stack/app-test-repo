<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class Test extends CI_Controller
{

    public function index()
    {
        $this->load->model('TestModel');
        $data = $this->TestModel->get_data();
        $this->output->set_content_type('application/json');
        $this->output->set_output(json_encode($data));
        $this->load->view('show_data', array('data' => $data));
        
    }
}