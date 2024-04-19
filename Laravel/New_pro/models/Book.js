const { random } = require("colors");
const mongoose = require("mongoose");
const { transliterate , slugify } =require("transliteration")
const BookSchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, "Book-iin name oruul "],
    unique: true,
    trim: true,
    maxlenght: [250, "250 тэмдэгт байх ёстой"],
  },
  photo: {
    type:String,
    default:"no-photo.jpg",

  },
  author:{
    type: String,
    required: [true, "Book-iin name oruul "],
    trim: true,
    maxlenght: [50, "250 тэмдэгт байх ёстой"],
  },
  rating:{
    type:Number,
    min:[1 ,"min bagadaa 1 bna"],
    max:[10,"max ihdee 10 bna "],
  },
  price:{
    type:Number,
    required: [true, "Book-iin price oruul "],
    min:[500 ,"Nomiin une hamgiin bagadaa 500 tug baina"],
  },
  balance:{
    type:Number,
  },
  content:{
    type: String,
    required: [true, "Book-iin contentiig oruul "],
    trim: true,
    maxlenght: [5000, "5000 тэмдэгт байх ёстой"],
  },
  bestseller:{
    type:Boolean,
    default:false
  },
  available: [String],
  category:{
    type: mongoose.Schema.ObjectId,
    ref:"Category",
    require: true
  },
  createAt:{
    type: Date,
    default:Date.now
  }
});


module.exports = mongoose.model("Book", BookSchema);
