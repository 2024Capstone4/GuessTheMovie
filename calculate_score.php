<?php
$titles = shell_exec("get_data.py");
echo($titles);
/*function get_scores($title){
    $critic_score = 0;
    $audience_score = 0;
    $imdb_score = 0;
    foreach($titles as $name){
        if ($name = $title)
            $critic_score = $name['tomatometer'];
            $audience_score = $name['audience_score'];
            $imdb_score = $name['imdb_score'];
    }
    
    return [$critic_score, $audience_score, $imdb_score];
}*/
function calculate_score($title, $critic_guess, $audience_guess, $imdb_guess) {
    $critic_actual = get_scores($title)[0];
    $audience_actual = get_scores($title)[1];
    $imdb_actual = get_scores($title)[2];
    $imdb_score = 100 - abs(($imdb_actual - $imdb_guess));
    $critic_score = 100 - abs(($critic_actual - $critic_guess));
    $audience_score = 100 - abs(($audience_actual - $audience_guess));
    $total_score = ($imdb_score + $critic_score + $audience_score)/3;
    return $total_score;
}



?>