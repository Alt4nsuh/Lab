const { random } = require("colors");
const mongoose = require("mongoose");
const { transliterate , slugify } =require("transliteration")
const CategorySchema = new mongoose.Schema({
  name: {
    type: String,
    required: [true, "Category-iin name oruul "],
    unique: true,
    trim: true,
    maxlenght: [50, "50 тэмдэгт байх ёстой"],
  },
  slug:String,
  description: {
    type: String,
    required: [true, "Category-iin description oruul "],
    maxlenght: [500, "500 тэмдэгт байх ёстой"],
  },
  photo: {
    type:String,
    default:"no-photo.jpg",

  },
  avarageRating:{
    type:Number,
    min:[1 ,"min bagadaa 1 bna"],
    max:[10,"max ihdee 10 bna "],

  },
  avaragePrice:{
    type:Number,
  },
  createAt:{
    type: Date,
    default:Date.now
  }
});

CategorySchema.pre('save', function(next) {
  // do stuff
  this.slug = slugify(this.name)
  this.avarageRating = Math.floor( Math.random()*10)+1
  this.avaragePrice = Math.floor( Math.random()*100000)+3000
  next();
});
module.exports = mongoose.model("Category", CategorySchema);
