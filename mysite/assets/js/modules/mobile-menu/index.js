import $ from 'jquery';

const desktopHeaderBreakpoint = 965;
const expandedHeaderBreakpoint = 775;
let currHeaderBreakpoint = desktopHeaderBreakpoint;

let headerMenuExpanded = false;
let sideMenuExpanded = false;

export default function addMenuResponsivity() {
	$('.mobile-nav__main').on('click', function() {
		// toggle arrow for header, ensure arrow up for sidemenu
		$('.mobile-nav__toggle__main').toggleClass('down');
		$('.mobile-nav__toggle__secondary').removeClass('down');

		// toggle header menu and ensure sidemenu hidden
		$('.mobile-header').toggle();
		$('.sidemenu-container').css('display', 'none');
		sideMenuExpanded = false;

		// if expanding header, hide content and footer, else show content and footer
		if (headerMenuExpanded) {
			$('.content-container').css('display', 'table-cell');
			$('footer').css('display', 'block');
			headerMenuExpanded = false;
		} else {
			$('.content-container').css('display', 'none');
			$('footer').css('display', 'none');
			headerMenuExpanded = true;
		}

	});

	$('.mobile-nav__secondary').on('click', function() {
		// toggle arrow for sidemenu, ensure arrow up for header
		$('.mobile-nav__toggle__secondary').toggleClass('down');
		$('.mobile-nav__toggle__main').removeClass('down');

		$('.mobile-sidemenu').css('display', 'block');
		$('.mobile-header').css('display', 'none');
		headerMenuExpanded = false;
		// sidemenuExpanded = !sidemenuExpanded;

		if (sideMenuExpanded) {
			$('.sidemenu-container').css('display', 'none');
			$('.content-container').css('display', 'table-cell');
			$('footer').css('display', 'block');
			sideMenuExpanded = false;
		} else {
			$('.sidemenu-container').css('display', 'table-cell');
			$('.content-container').css('display', 'none');
			$('footer').css('display', 'none');
			sideMenuExpanded = true;
		}
	});

	currHeaderBreakpoint = $('body').hasClass('header--expanded') ? expandedHeaderBreakpoint : desktopHeaderBreakpoint;

	addResizeListener();

		$('.mobile-menu__link__main a')
			.on('click', function() {
				$(this).siblings('.rotate').toggleClass('down');
			});

		$('.mobile-header .mobile-menu__link__main a')
			.on('mouseover', function() {
				$(this).siblings('.rotate').removeClass('flip-arrow-black').addClass('flip-arrow-white');
			})
			.on('mouseout', function() {
				console.log($(this).context.offsetParent);
				$(this).siblings('.rotate').removeClass('flip-arrow-white').addClass('flip-arrow-black');
			});
}

function addResizeListener() {
	const resizeMediaQuery = window.matchMedia('(min-width: ' + currHeaderBreakpoint + 'px)');
		resizeMediaQuery.addListener(WidthChange);
		WidthChange(resizeMediaQuery);
}

function WidthChange(mq) {

  if (mq.matches) {
	$('.mobile-nav').css('display', 'none');
	$('.mobile-header').css('display', 'none');
	$('.mobile-sidemenu').css('display', 'none');
	$('.sidemenu').css('display', 'block');
	$('.sidemenu-container').css('display', 'table-cell');
	$('.content-container').css('display', 'table-cell');
	$('footer').css('display', 'block');
	sideMenuExpanded = false;
	headerMenuExpanded = false;
  } else {
	$('.mobile-nav').css('display', 'block');
	$('.sidemenu').css('display', 'none');

	if (!sideMenuExpanded) {
		$('.sidemenu-container').css('display', 'none');
		$('.content-container').css('display', 'block');
	}
	if (!headerMenuExpanded) {
		$('.mobile-header').css('display', 'none');
	}
  }

}
