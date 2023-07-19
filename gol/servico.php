<?php

    $data = file_get_contents('php://input');
    $obj = json_decode( $data, true );
    $sql = "select origem, destino, datahora from voo";
    $conexao = new pdo('sqlite:banco.sqlite');
    $resultado = $conexao->query($sql)->fetchAll();
    $data = json_encode( $resultado );
    print $data;