var content_offtop = $('.article-content').offset().top;
var content_height = $('.article-content').innerHeight();
$(window).scroll(function () {
 if (($(this).scrollTop() > content_offtop)) { //滑动到内容部分
 if (($(this).scrollTop() - content_offtop) <= content_height) { //在内容部分内滑动
 this.reading_p = Math.round(($(this).scrollTop() - content_offtop) / (content_height-500) * 100);
 } else { //滑出内容部分
 this.reading_p = 100; //确保进度条铺满
 }
 } else { //未滑到内容部分
 this.reading_p = 0; //确保进度条不显示
 }
 $('.progressIndicator').css('width', this.reading_p + '%');
});