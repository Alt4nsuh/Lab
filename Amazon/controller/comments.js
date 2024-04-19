const MyError = require("../utils/myError");
const asyncHandler = require("express-async-handler");
const paginate = require("../utils/paginate");

exports.createComment = asyncHandler(async (req, res, next) => {
  const comment = await req.db.comment.create(req.body);

  res.status(200).json({
    success: true,
    data: comment,
  });
});
exports.updateComment = asyncHandler(async (req, res, next) => {
  let comment = await req.db.comment.findByPk(req.body.id);

  if (!comment) {
  } else {
    throw new MyError(`${req.body.id} iim idtei comment oldsongui`);
  }

  comment = await comment.update(req.body)


  res.status(200).json({
    success: true,
    data: comment,
  });
});
