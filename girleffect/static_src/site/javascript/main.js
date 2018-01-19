import $ from './globals';
import 'owl.carousel';
import 'scrolltofixed';
import 'featherlight';

import Hamburger from './../patterns/00-atoms/buttons/hamburger/hamburger.js';

// Open the header callback
function openHeader() {
    $('.header')
        .addClass('nav-open')
        .find('.header__row')
        .fadeIn(250);
}

// Close the header callback.
function closeHeader() {
    $('.header')
        .removeClass('nav-open')
        .find('.header__row')
        .fadeOut(250, () => {
            this.node.next().removeAttr('style');
        });
}

$(function() {
    $(Hamburger.selector()).each((index, el) => {
        new Hamburger($(el), openHeader, closeHeader);
    });

    // Autoplays YouTube embed in a video streamfield
    $('.video__button').on('click', function(ev) {
        const video = $(this)
            .parent()
            .siblings()
            .find('iframe');
        const overlay = $(this).parent('.video__overlay');
        $(video)[0].src += '&autoplay=1&modestbranding=1&showinfo=0';
        $(overlay).hide();
        ev.preventDefault();
    });

    // Full width slider streamfield
    $('.js-carousel--full-width').owlCarousel({
        items: 1,
        nav: true,
        dots: true,
        autoHeight: false,
        navContainer: '.js-full-width-nav',
        navText: [
            '<svg class="carousel__nav-left"><use xlink:href="#arrow"></use></svg>',
            '<svg class="carousel__nav-right"><use xlink:href="#arrow"></use></svg>'
        ],
        loop: $('.owl-carousel .carousel__item').length > 1 ? true : false
    });

    // Full width slider streamfield
    $('.js-slider--full-width').owlCarousel({
        items: 1,
        nav: true,
        dots: true,
        autoHeight: false,
        navContainer: '.js-slider__nav--full-width',
        navText: [
            '<svg class="slider__nav-left"></svg>',
            '<svg class="slider__nav-right"></svg>'
        ],
        loop: true,
        autoplay: $('.slider-container').attr('data-delay') > 0,
        autoplayTimeout: $('.slider-container').attr('data-delay')
    });

    // Hide the carousel nav if there's only one slide - relies on the result of the loop ternary above
    if ($('.owl-carousel .carousel__item').length === 1) {
        $('.carousel__nav').hide();
    }

    // Filters articles via the category id
    $('.js-article-filter').on('change', function() {
        var url = $(this).val();

        if (url) {
            window.location = `?category=${url}`;
            return false;
        }
        window.location = '/stories/';
        return false;
    });

    // Modal that autoplays a YouTube embed
    $('.js-modal').featherlight({
        targetAttr: 'href',
        variant: 'modal-container', // add class for custom styling
        afterOpen: () => {
            const video = $('.featherlight iframe')[0];
            video.src += '&autoplay=1&modestbranding=1&showinfo=0';
        }
    });

    // Desktop search
    $('.js-search-desktop').on('click', function() {
        $(this).toggleClass('is-is-active');
        const headerHeight = $('.header').outerHeight();
        const searchBar = $('.header__search-bar--desktop');
        const form = $('.form--search');

        $(searchBar).css('top', headerHeight); // get the header height so the search bar displays in the correct place
        $(form).removeClass('visible');
        $(searchBar).slideToggle(250, function() {
            $(form).addClass('visible');
            $('.input--search').focus();
        });
    });

    // Mobile search open
    $('.js-search-mobile').on('click', function() {
        $('.header__search-bar--mobile').addClass('is-visible');
        $('.input--search').focus();
    });

    // Mobile search close
    $('.js-close-search-mobile').on('click', function() {
        $('.header__search-bar--mobile').removeClass('is-visible');
    });

    // Sticky share icons on the article page
    if ($('.js-share-icons').length) {
        $('.js-share-icons').scrollToFixed({
            marginTop: 30,
            limit:
                $($('.footer')).offset().top -
                $('.js-share-icons').outerHeight(true) -
                30
        });
    }

    // Desktop navigation
    if (window.matchMedia('(min-width: 1024px)').matches) {
        $('.header__nav-item-primary-parent, .header__nav-secondary').mouseover(
            function() {
                $(this)
                    .children('.header__link-primary')
                    .addClass('is-is-active');
                $(this)
                    .children('.header__nav-secondary')
                    .addClass('is-visible');
                $('.header__nav-overlay').addClass('is-visible');
            }
        );

        $(
            '.header__nav-item-primary-parent, .header__nav-overlay, .header__nav-secondary'
        ).mouseout(function() {
            $(this)
                .children('.header__link-primary')
                .removeClass('is-is-active');
            $('.header__nav-overlay, .header__nav-secondary').removeClass(
                'is-visible'
            );
        });
    }

    // Mobile navigation
    if (window.matchMedia('(max-width: 1024px)').matches) {
        $('.header__link-primary').on('click', function() {
            $(this)
                .parent()
                .toggleClass('is-open');
            $(this)
                .siblings('ul')
                .slideToggle(250);
        });

        $('.js-mobile-dropdown').on('click', function() {
            $(this)
                .parent()
                .toggleClass('is-open');
            $(this)
                .next('ul')
                .slideToggle(250);
        });
    }

    // Home page carousel - changes to Owl Carousel on mobile
    $('.carousel__panel').mouseover(function() {
        const panelNumber = $(this).data('panel');
        const image = document.querySelector(
            `img[data-image="${panelNumber}"]`
        );
        $('.carousel__panel').removeClass('is-expanded');
        $(this).addClass('is-expanded');

        this.addEventListener('transitionend', function(e) {
            if (e.propertyName !== 'height') return;
            $(this)
                .children('.carousel__panel-content')
                .css('opacity', 1);
        });

        $('.carousel__image--hidden').removeClass('is-visible');
        $(image).addClass('is-visible');
    });

    // Always show the main slide when not hovering on the home page carousel
    $('.carousel--home-desktop').mouseout(function() {
        $('.carousel__image.is-visible').removeClass('is-visible');
    });

    // Hide the carousel panels when not being hovered over
    $('.carousel__panel').mouseout(function() {
        $('.carousel__panel').removeClass('is-expanded');
    });

    // Home page carsouel on mobile
    $('.js-carousel--home-mobile').owlCarousel({
        items: 1,
        nav: false,
        dots: true
    });

    // Article Page Filter Setup
    function constructFilter(filter) {
        filter.addClass('article-select--hidden');
        filter.wrap('<div class="article-select"></div>');
        filter.after('<div class="article-select--styled"></div>');
    }

    function defaultFilterItem(filter) {
        var styledArticleFilter = filter.next('div.article-select--styled');
        styledArticleFilter.text(
            $('option[selected]').text() ||
                filter
                    .children('option')
                    .eq(0)
                    .text()
        );

        return styledArticleFilter;
    }

    function createFilterListItems(
        articleFilter,
        articleFilterOptionsCount,
        filterList
    ) {
        for (var i = 0; i < articleFilterOptionsCount; i++) {
            $('<li />', {
                text: articleFilter
                    .children('option')
                    .eq(i)
                    .text(),
                rel: articleFilter
                    .children('option')
                    .eq(i)
                    .val(),
                class:
                    articleFilter
                        .children('option')
                        .eq(i)
                        .val() === $('option[selected]').val()
                        ? 'is-selected'
                        : null
            }).appendTo(filterList);
        }
    }

    function createFilterList(styledArticleFilter) {
        return $('<ul />', {
            class: 'article-select__options'
        }).insertAfter(styledArticleFilter);
    }

    function setDefaultSelectedFilterItem(filterList) {
        var selectedItems = filterList.children('.is-selected');
        if (selectedItems.length === 0) {
            $(filterList.children('li')[0]).addClass('is-selected');
        }
    }

    $('.js-article-filter').each(function() {
        const articleFilter = $(this);
        const articleFilterOptionsCount = articleFilter.children('option')
            .length;
        constructFilter(articleFilter);
        const styledArticleFilter = defaultFilterItem(articleFilter);
        const filterList = createFilterList(styledArticleFilter);
        createFilterListItems(
            articleFilter,
            articleFilterOptionsCount,
            filterList
        );
        const filterListItems = filterList.children('li');
        setDefaultSelectedFilterItem(filterList);

        styledArticleFilter.click(function(e) {
            e.stopPropagation();
            $('div.article-select--styled.is-active')
                .not(this)
                .each(function() {
                    $(this)
                        .removeClass('is-active')
                        .next('ul.select__options')
                        .hide();
                });
            $(this)
                .toggleClass('is-active')
                .next('ul.article-select__options')
                .toggle();
        });

        filterListItems.click(function(e) {
            e.stopPropagation();
            styledArticleFilter.text($(this).text()).removeClass('is-active');
            $(articleFilter.children('option[selected]')).attr(
                'selected',
                false
            );
            if ($(this).attr('rel')) {
                $(`option[value=${$(this).attr('rel')}]`).attr(
                    'selected',
                    'selected'
                );
            } else {
                $(filterListItems[0]).attr('selected', 'selected');
            }

            $('form').submit();
        });

        $(document).click(function() {
            styledArticleFilter.removeClass('is-active');
            filterList.hide();
        });
    });
});
