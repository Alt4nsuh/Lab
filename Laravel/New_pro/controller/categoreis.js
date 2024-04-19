const Category = require("../models/Category");
const MyError = require("../utils/myError");
const asyncHandler = require("../middleware/asyncHandler");
exports.getCategories = asyncHandler(async (req, res, next) => {
  const limit = parseInt(req.query.limit) || 100;
  const page = parseInt(req.query.page) || 1;
  const select = req.query.select;
  const sort = req.query.sort;

  ["limit","page","sort","select"].forEach((el)=>delete req.query[el])
  //----
  const total =await Category.countDocuments();
  const pageCount = Math.ceil(total/limit)
  const start = (page-1)*limit+1
  const end = start + limit - 1;
  const end2 = total;
  const pagination = {
    total,
    pageCount: Math.ceil(total / limit),
    start,
    end: end > total ? end : end2,
    limit
  };
  if(page<pageCount) pagination.nextPage = page+1;
  if(page>1) pagination.prevPage = page-1;

  const category = await Category.find(req.query,select)
    .sort(sort)
    .skip(start-1)
    .limit(limit);

  console.log(req.query,select);
  res.status(200).json({
    success: true,
    data: category,
    pagination
  });
});

exports.getCategory = asyncHandler(async (req, res, next) => {
  const category = await Category.findById(req.params.id);
  if (!category) {
    throw new MyError(req.params.id + "iim hereglegch baihgui", 400);
  }
  res.status(200).json({
    success: true,
    data: category,
  });

  next(err);
});

exports.createCategories = asyncHandler(async (req, res, next) => {
  const category = await Category.create(req.body);
  console.log("data", req.body);

  res.json({
    success: true,
    data: category,
  });

  next(err);
});

exports.updateCategories = asyncHandler(async (req, res, next) => {
  const category = await Category.findByIdAndUpdate(req.params.id, req.body, {
    new: true,
    runValidators: true,
  });
  if (category) {
    throw new MyError(req.params.id + "iim hereglegch baihgui", 400);
  }
  res.status(200).json({
    success: true,
    data: category,
  });

  next(err);
});

exports.deleteCategories = asyncHandler(async (req, res, next) => {
  const category = await Category.findByIdAndDelete(req.params.id);
  if (category) {
    throw new MyError(req.params.id + "iim hereglegch baihgui", 400);
  }
  res.status(200).json({
    success: true,
    data: category,
  });
  next(err);
});
