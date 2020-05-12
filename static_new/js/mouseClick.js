/* 鼠标特效 */

var a_idx = 0;

jQuery(document).ready(function($) {
$("body").click(function(e) {
    var a = new Array("不要停下来啊", "你在干什么啊，团长", "我也是加把劲骑士", "一直以来的努力都没有白费", "大家都在等你", "只要我们不停下来", "前面一定会有路" ,"所以，不要停下来啊", "希望之花");
    var $i = $("<span/>").text(a[a_idx]);
    a_idx = (a_idx + 1) % a.length;
    var x = e.pageX,
    y = e.pageY;
    $i.css({
        "z-index": 999999999999999999999999999999999999999999999999999999999999999999999,
        "top": y - 20,
        "left": x,
        "position": "absolute",
        "font-weight": "bold",
        "color": "#ff6651"
    });
    $("body").append($i);
    $i.animate({
        "top": y - 180,
        "opacity": 0
    },
    1500,
    function() {
        $i.remove();
    });
});
});
