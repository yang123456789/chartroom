$(function() {
    // 首页tab切换
    var head = $('.login .header ul li');
    head.on('click', function () {
        $(this).addClass('title').siblings().removeClass('title');
    });
});