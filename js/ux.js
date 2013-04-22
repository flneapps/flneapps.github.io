
function ux(){
	$(".intro .more").toggle(function(){
		$(".introMore").slideDown();
	}, function(){
		$(".introMore").slideUp();
	})

	$(".onoff img").click(function(){
		//var thisSrc = $(this).attr("src");
		//$(this).attr("src", thisSrc.replace("_off", "_on"));
	})

	$(".agree").toggle(function(){
		$(this).removeClass("on");
		$(this).addClass("on");
	}, function(){
		$(this).removeClass("on");
	})

	if(!$(".progerss").is(":hidden")){
		$(".title").css("z-index", "70");
		$(".appListSection").css("z-index", "70");
	}

	$(".tab a img").click(function(){
		var thisSrc = $(this).attr("src");
		$(".tab a img").each(function(){
			var thisSrc = $(this).attr("src");
			$(this).attr("src", thisSrc.replace("_on", "_off"));
		})
		$(this).attr("src", thisSrc.replace("_off", "_on"));
	});

	$(".popup .close").click(function(){
		//var thisSrc = $(this).children().attr("src");
		//$(this).children().attr("src", thisSrc.replace(".png", "_on.png"));

		$(".popup, .pageMask").hide();
	});

	$(".appList li").each(function(){
		var _this =$(this)
		_this.find(".onMask").click(function(){
			_this.append("<span class='on'></span>");
		})
	});

	$(".appList2 li").each(function(){
		var _this =$(this)
		_this.find(".onMask").click(function(){
			_this.append("<span class='on'></span>");
		})
	});

	$(".listType1 li, .listType2 li").click(function(){
		$(this).toggleClass("over")
	});
}

$(function(){
	ux();
})