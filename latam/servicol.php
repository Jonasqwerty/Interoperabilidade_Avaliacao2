<?php

    $data = file_get_contents('php://input');
    $obj = json_decode( $data, true );
    $conexao = new pdo('sqlite:database');
    $origem = $obj["origem"];
    $destino = $obj["destino"];
    $datahora = $obj["datahora"];
    
    if ($origem){
        $select = " select * from vvoo where origem='$origem' and destino='$destino' and datahora='$datahora' ; ";
        $resultado = $conexao->query($select)->fetchAll();
        $result = json_encode($resultado);
        error_log($result);
        print $result;
        return;
    }
    $select = " select * from vvoo; ";
    $resultado = $conexao->query($select)->fetchAll();
    $result = json_encode( $resultado );
    print $result;

