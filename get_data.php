<?php

// URL of the JSONbin endpoint
$url = 'https://api.jsonbin.io/v3/b/65d77e13266cfc3fde8ddeb7/latest/';

// Headers for authentication
$headers = array(
    'X-Master-Key: $2a$10$vaoE2zeHNzxtHNFsBwBw7uMzvHzDdHKlB2xwIn0yBJy3.0fKO0JhG',
    'X-Bin-Meta: false'
);

// Initialize cURL session
$ch = curl_init();

// Set cURL options
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);

// Execute cURL session
$response = curl_exec($ch);

// Close cURL session
curl_close($ch);

// Check if request was successful
if ($response === false) {
    echo 'Error: Failed to fetch data.';
} else {
    // Decode JSON response
    $data = json_decode($response, true);
    
    // Check if decoding was successful
    if ($data === null) {
        echo 'Error: Failed to decode JSON.';
    } else {
        // Access the data as an array
        // Example: $data['key'] or $data[0]['key']
        // Display the data (for testing)
        var_dump($data);
    }
}
?>
