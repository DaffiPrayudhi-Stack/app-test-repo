<?php
defined('BASEPATH') OR exit('No direct script access allowed');
?><!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Welcome to CodeIgniter</title>
    <script src="https://cdn.datatables.net/2.3.3/js/dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/2.3.3/js/dataTables.bootstrap.min.js"></script>
    <link rel="stylesheet" href="https://cdn.datatables.net/2.3.3/css/dataTables.dataTables.min.css">
</head>
<body>
    <h1>History Data</h1>
    <table id="tableid" class="table table-striped table-bordered" style="width:100%">
        <thead>
            <tr>
                <th>Date</th>
                <th>Data</th>
                <th>Qty</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($data as $row) { ?>
                <tr>
                    <td><?= $row->tanggal ?></td>
                    <td><?= $row->nama ?></td>
                    <td><?= $row->qty ?></td>
                </tr>
            <?php } ?>
        </tbody>
    </table>
    
    <script>
        $(document).ready(function() {
            s.ajax({
                type: 'GET',
                url: '<?php echo base_url('test/index'); ?>',
                dataType: 'json',
                success: function(data) {
                    var table = $('#tableid').DataTable({
                    data: data,
                    columns: [
                        { data: 'tanggal' },
                        { data: 'nama' }
                    ]
                    });
                }
            })
        }
    )
    </script>

</body>
</html>