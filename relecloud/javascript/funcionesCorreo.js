function sendEmail() {
    // Configura la información del servidor SMTP
    Email.server = {
        Host: "smtp.office365.com",
        Username: "pedri_julian@outlook.es",
        Password: "Constan12",
        Port: 587,
    };

    // Configura el correo electrónico que se enviará
    Email.send({
        To: 'jmgarciab2@gmail.com',
        From: "pedri_julian@outlook.es",
        Subject: "Confirmación Solicitud",
        Body: "Se ha aprobado con éxito su solicitud!",
    }).then(
        message => alert("Email sent successfully: " + message),
        error => alert("Error sending email: " + error)
    );
}