<html>
<head>
    <title>SQL Injection</title>
</head>
<body>
    <form action="sql_injection.php" method="post">
        Enter RegNo:&nbsp;<input type=text id="username" name="username"><br>
        Enter password:&nbsp;<input type=password id="password" name="password"><br>
        <input type="submit" value="Submit">
    </form>
    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $servername = "localhost";
        $username = "root";
        $password = "Sid_12345";
        $dbname = "test";

        $conn = new mysqli($servername, $username, $password, $dbname);

        if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
        }

        $user = $_POST["username"];
        $pass = $_POST["password"];
        $sql = "SELECT * FROM student where RegNo = '$user' and Password ='$pass' ";
        $result = $conn->query($sql);
        if ($result->num_rows > 0) {
            echo "Login Successful";
        } else {
            echo "Failed Login";
        }
    }
    ?>
</body>
</html>
