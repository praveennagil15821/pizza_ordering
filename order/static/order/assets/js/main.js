(function($) {
  'use strict';

  /*-------------------------------------------------------------------------------
  Preloader
	-------------------------------------------------------------------------------*/
  $(window).on('load', function() {
    $('.ct-preloader').addClass('hidden');
  });

  /*-------------------------------------------------------------------------------
  Aside Menu
	-------------------------------------------------------------------------------*/
  $(".aside-trigger").on('click', function() {
    $(".main-aside").toggleClass('open');
  });
  $(".main-aside .menu-item-has-children > a").on('click', function(e) {
    var submenu = $(this).next(".submenu");
    e.preventDefault();

    submenu.slideToggle(200);
  })

  /*-------------------------------------------------------------------------------
  Cart Trigger
  -------------------------------------------------------------------------------*/
  $(".cart-trigger").on('click', function(e) {
    $("body").toggleClass('cart-open');
  });
   /*-------------------------------------------------------------------------------
  Login Trigger
  -------------------------------------------------------------------------------*/
  // $(".cart-trigger").on('click', function(e) {
  //   $("body").toggleClass('cart-open');
  // });

  
  /*-------------------------------------------------------------------------------
  Checkout Notices
  -------------------------------------------------------------------------------*/
  $(".ct-notice a").on('click', function(e){
    e.preventDefault();

    $(this).closest('.ct-notice').next().slideToggle();
  });

  
  /*-------------------------------------------------------------------------------
  Sticky Header
	-------------------------------------------------------------------------------*/
  function doSticky() {
    var header = $(".can-sticky");

    if (window.pageYOffset > 50) {
      header.addClass("sticky");
    } else {
      header.removeClass("sticky");
    }
  }
  doSticky();

  /*-----------------------------------
    Back to Top
    -----------------------------------*/
  $('.back-to-top').on('click', function() {
    $("html, body").animate({
      scrollTop: 0
    }, 600);
    return false;
  })
  /*-----------------------------------
    Back to Login
    -----------------------------------*/
    $('.back-to-login').on('click', function() {
      $("html, body").animate({
        scrollTop: 350
      }, 600);
      $('.at-login').click();
      return false;
    })
    

  /*-------------------------------------------------------------------------------
  Aside Scroll
	-------------------------------------------------------------------------------*/
  function initAsideScrollbar() {
    var scrollHeight = $('.main-aside').innerHeight() - $(".main-aside .navbar-brand").innerHeight(); // Calculate the height of the scroll container
    var calculatedHeight = isNaN(scrollHeight) ? "auto" : scrollHeight;
    $('.aside-scroll').slimScroll({
      height: calculatedHeight,
      position: "right",
      size: "5px",
      color: "#dcdcdc",
      opacity: 1,
      wheelStep: 5,
      touchScrollStep: 50,
    });
  }
  initAsideScrollbar();

  /*-------------------------------------------------------------------------------
  Cart Scroll
  -------------------------------------------------------------------------------*/
  function initCartScrollbar() {
    var scrollHeight = $('.cart-sidebar').innerHeight() - $(".cart-sidebar .cart-sidebar-header").innerHeight() - $(".cart-sidebar .cart-sidebar-footer").innerHeight() - 40; // Calculate the height of the scroll container
    var calculatedHeight = isNaN(scrollHeight) ? "auto" : scrollHeight;
    $('.cart-sidebar-scroll').slimScroll({
      height: calculatedHeight,
      position: "right",
      size: "5px",
      alwaysVisible: true,
      color: "#4e4e4e",
      railVisible: true,
      railColor: '#212222',
      opacity: 1,
      wheelStep: 5,
      touchScrollStep: 50,
    });
  }
  initCartScrollbar();

  /*-------------------------------------------------------------------------------
  Tooltips
  -------------------------------------------------------------------------------*/
  $('[data-toggle="tooltip"]').tooltip();

  /*-------------------------------------------------------------------------------
  Magnific Popup
  -------------------------------------------------------------------------------*/
  $('.popup-youtube').magnificPopup({
    type: 'iframe'
  });
  $('.popup-vimeo').magnificPopup({
    type: 'iframe'
  });
  $('.popup-video').magnificPopup({
    type: 'iframe'
  });
  $('.gallery-thumb').magnificPopup({
    type: 'image',
    gallery: {
      enabled: true
    },
  });

  
  /*-------------------------------------------------------------------------------
  Masonry
  -------------------------------------------------------------------------------*/
  $('.masonry').imagesLoaded(function() {
    var isotopeContainer = $('.masonry');
    isotopeContainer.isotope({
      itemSelector: '.masonry-item',
    });
  });

  /*-------------------------------------------------------------------------------
  Add / Subtract Quantity
  -------------------------------------------------------------------------------*/
  // $(".qty span").on('click', function(){
  //   var qty = $(this).closest('.qty').find('input');
  //   var qtyVal = parseInt(qty.val());
  //   if($(this).hasClass('qty-add')){
  //     qty.val(qtyVal + 1);
  //   }else{
  //     return qtyVal > 1 ? qty.val(qtyVal - 1) : 0;
  //   }
  // })
  $(".qty span").on('click', function(){
    var qty = $(this).closest('.qty').find('input');
    var qtyVal = parseInt(qty.val());
    // var txt = $(".pricety span").closest('.pricety').find('input');
    // alert(txt.val());
    if($(this).hasClass('qty-add')){
      qty.val(qtyVal + 1);
    }else{
      return qtyVal > 1 ? qty.val(qtyVal - 1) : 0;
    }
  });




  
  //On scroll events
  $(window).on('scroll', function() {

    doSticky();

  });

  //On resize events
  $(window).on('resize', function() {

    initAsideScrollbar();
    initCartScrollbar();

  });

})(jQuery);
