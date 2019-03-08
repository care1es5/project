<?php
  ini_set('display_errors', 'On');
  error_reporting(E_ALL | E_STRICT);
  echo "<html>";
  if (isset($_POST["username"]) && isset($_POST["password"])) {
    $servername = "localhost";
    $username = "sqli-user";
    $password = 'AxU3a9w-azMC7LKzxrVJ^tu5qnM_98Eb';
    $dbname = "SqliDB";
    $conn = new mysqli($servername, $username, $password, $dbname);
    if ($conn->connect_error)
        die("Connection failed: " . $conn->connect_error);
    
    $conn->set_charset("utf8mb4");

    $user = $_POST['username'];
    $pass = $_POST['password'];
   
    $stmt = $conn->prepare("SELECT * FROM login WHERE User = ? AND Password = ?");

    $stmt->bind_param("ss", $user,$pass);
	
    $stmt->execute();
    
    $result = $stmt->get_result();

    if ($result->num_rows >= 1)
    {
        $row = $result->fetch_assoc(); 
        echo "You logged in as " . $row["User"];
        $row = $result->fetch_assoc();
        echo "<html>You logged in as " . $row["User"] . "</html>\n";
    }
    else {
        echo "Sorry to say, that's invalid login info!";
    }
    $conn->close();
  }
  else
    echo "Must supply username and password...";
  echo "</html>";
?>
