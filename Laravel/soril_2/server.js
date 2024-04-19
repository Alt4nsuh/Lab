
const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');

const app = express();
const PORT = process.env.PORT || 5000;

mongoose.connect('mongodb://localhost:27017/forms', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});
const db = mongoose.connection;

db.once('open', () => console.log('Connected to MongoDB'));
db.on('error', err => console.error('MongoDB connection error:', err));

const userSchema = new mongoose.Schema({
  lastname: String,
  firstname: String,
});

const User = mongoose.model('User', userSchema);


app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/submit', (req, res) => {
  const { lastname, firstname } = req.body;
  
  const newUser = new User({ lastname, firstname });
  
  newUser.save()
    .then(() => res.json({ message: 'Form submitted successfully' }))
    .catch(err => res.status(500).json({ error: err.message }));
});

app.listen(PORT, () => console.log(`Server is running on http://localhost:${PORT}`));
