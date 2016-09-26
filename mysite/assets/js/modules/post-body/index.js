import $ from 'jquery';
/*

Removes dropcap if first paragraph character count is less than cutoff character limit

*/
function checkDropcap() {
	var dropcapCutoff = 300;
	var $first_paragraph = $(".with-dropcap > .block-paragraph:first-child p:first-child");
	var paragraphLength = $first_paragraph.text().length;

	if (paragraphLength < dropcapCutoff) {
		$(".with-dropcap").removeClass("with-dropcap");
	}
}

function convertToHttps() {
	$('.post-body').find('iframe').each( function() {
		var source = $(this).prop('src');
		var newSource = source.replace('http:', 'https:');
		$(this).prop('src', newSource);
	});
		
}

function addDatavizDownloadInteractivity() {
	// $(".dataviz__download-link")
	// 	.on("click", function() {
	// 		$(this).siblings(".dataviz__download-popup").show();
	// 	});

	// $(".dataviz__download-popup").on("mouseleave", function() {
	// 	$(this).hide();
	// });
}

function resizeTableBlock() {
	$(document).ready(setTableWidth);
	$(window).resize(setTableWidth);

	function setTableWidth() {
		var $contentContainer = $(".content-container");
		var $body = $("body")
		var bodyWidth = $body.width();

		if ($contentContainer.hasClass("has-sidemenu") && (bodyWidth > 965)) {
			$(".block-table").width(bodyWidth - 300);
		} else if ($body.hasClass("template-indepthsection") || $body.hasClass("template-indepthproject")) {
			$(".block-table").width(bodyWidth - 100);
		} else {
			$(".block-table").width(bodyWidth - 50);
		}
	}
}

export default function() {
	checkDropcap();
	convertToHttps();
	addDatavizDownloadInteractivity();
	resizeTableBlock();
}