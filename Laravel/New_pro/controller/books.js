const Book = require("../models/Book");
const MyError = require("../utils/myError");
const asyncHandler = require("../middleware/asyncHandler");
exports.getBooks = asyncHandler(async (req, res, next) => {
  let query;
  if(req.params.catId){
    query = Book.find({category: req.params.catId} )
  }else{
    query =  Book.find()
  }
  const Books = await query
  res.status(200).json({
    success: true,
    count: Books.length,
    data: Books,
  });
});

exports.getBook = asyncHandler(async (req, res, next) => {
  const Books = await Book.findById(req.params.id);
  if (!Books) {
    throw new MyError(req.params.id + "iim hereglegch baihgui", 400);
  }
  res.status(200).json({
    success: true,
    data: Books,
  });

  next(err);
});

exports.createBooks = asyncHandler(async (req, res, next) => {
  const Book = await Book.create(req.body);
  console.log("data", req.body);

  res.json({
    success: true,
    data: Book,
  });

  next(err);
});

exports.updateBooks = asyncHandler(async (req, res, next) => {
  const Book = await Book.findByIdAndUpdate(req.params.id, req.body, {
    new: true,
    runValidators: true,
  });
  if (Book) {
    throw new MyError(req.params.id + "iim hereglegch baihgui", 400);
  }
  res.status(200).json({
    success: true,
    data: Book,
  });

  next(err);
});

exports.deleteBooks = asyncHandler(async (req, res, next) => {
  const Book = await Book.findByIdAndDelete(req.params.id);
  if (Book) {
    throw new MyError(req.params.id + "iim hereglegch baihgui", 400);
  }
  res.status(200).json({
    success: true,
    data: Book,
  });
  next(err);
});
