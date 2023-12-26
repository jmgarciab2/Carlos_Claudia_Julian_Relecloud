const nodemailer = require('nodemailer');

function sendEmail() {
  // Configura la información del servidor SMTP
  const transporter = nodemailer.createTransport({
    host: 'smtp.office365.com',
    port: 587,
    secure: false,
    auth: {
      user: 'pedri_julian@outlook.es',
      pass: 'Constan12',
    },
  });

  // Configura el correo electrónico que se enviará
  const mailOptions = {
    from: 'pedri_julian@outlook.es',
    to: 'jmgarciab2@gmail.com',
    subject: 'Confirmación Solicitud',
    text: 'Se ha aprobado con éxito su solicitud!',
  };

  // Envía el correo electrónico
  transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
      return console.error('Error al enviar el correo:', error);
    }
    console.log('Correo electrónico enviado:', info.response);
  });
}
