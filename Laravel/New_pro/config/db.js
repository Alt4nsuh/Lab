const mongoose = require("mongoose");

const connectDB = async () => {

    const conn = await mongoose.connect(process.env.MONGODB_URI, {
    });
    console.log(`Connected to MongoDB: ${conn.connection.host}`.cyan);
  
};

module.exports = connectDB;
