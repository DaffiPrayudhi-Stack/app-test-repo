<?php

defined('BASEPATH') OR exit('No direct script access allowed');

class TestModel extends CI_Model {

    public function __construct() {
        parent::__construct();
        $this->load->database();
    }

    public function get_data_by_date($past_date) {
        $this->db->select('*');
        $this->db->from('showdata');
        $this->db->where('tanggal >=', $past_date);
        $this->db->where('tanggal <=', date('Y-m-d'));
        $this->db->order_by('tanggal', 'DESC');
        $query = $this->db->get();
        return $query->result();
    }

     public function get_data () {
        $this->db->select('*');
        $this->db->from('showdata');
        $query = $this->db->get();
        return $query->result();
    }

}