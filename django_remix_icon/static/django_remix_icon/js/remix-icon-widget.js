/**
 * Django Remix Icon Widget JavaScript with Select2 Integration
 * Provides beautiful search interface and icon previews
 */

(function($) {
    'use strict';

    function initRemixIconWidget() {
        // Wait for all scripts to load
        if (!$ || !$.fn.select2) {
            setTimeout(initRemixIconWidget, 100);
            return;
        }

        // Initialize Select2 for remix icon selects
        $('.remix-icon-select[data-widget="remix-icon"]').each(function() {
            const $select = $(this);

            // Skip if already initialized
            if ($select.hasClass('select2-hidden-accessible')) {
                return;
            }

            // Store the original value before any manipulation
            const originalValue = $select.find('option[selected]').val() || $select.val() || $select.attr('data-current-value');

            // Initialize Select2
            $select.select2({
                placeholder: 'Choose a Remix Icon...',
                allowClear: true,
                width: '100%',
                templateResult: formatIcon,
                templateSelection: formatIconSelection,
                escapeMarkup: function(markup) {
                    return markup;
                }
            });

            // Handle clear event
            $select.on('select2:clear', function(e) {
                // Ensure the value is actually cleared
                $(this).val('').trigger('change');
            });

            // Handle selection change for proper clearing
            $select.on('select2:select select2:unselect', function(e) {
                // Trigger change event for Django forms
                $(this).trigger('change');
            });

            // Immediately set the value after initialization
            if (originalValue && originalValue !== '' && originalValue !== 'None') {
                // First ensure the option exists and is selected in the original select
                $select.find('option').prop('selected', false);
                $select.find('option[value="' + originalValue + '"]').prop('selected', true);

                // Then update Select2
                $select.val(originalValue).trigger('change.select2');
            }
        });
    }

    function formatIcon(icon) {
        if (!icon.id || icon.id === '') {
            return icon.text;
        }

        const iconValue = icon.id;
        return $(`
            <div class="remix-icon-option">
                <i class="ri-${iconValue}"></i>
                <span class="icon-name">${icon.text}</span>
            </div>
        `);
    }

    function formatIconSelection(icon) {
        if (!icon.id || icon.id === '') {
            return icon.text;
        }

        const iconValue = icon.id;
        return $(`
            <div class="remix-icon-selection">
                <i class="ri-${iconValue}"></i>
                <span class="icon-name">${iconValue}</span>
            </div>
        `);
    }

    // Multiple initialization attempts for safety
    $(document).ready(function() {
        setTimeout(initRemixIconWidget, 50);
        setTimeout(initRemixIconWidget, 200);
        setTimeout(initRemixIconWidget, 500);
    });

    $(window).on('load', function() {
        setTimeout(initRemixIconWidget, 100);
    });

    function loadSelect2() {
        // Load Select2 CSS
        if (!$('link[href*="select2"]').length) {
            $('<link>')
                .attr('rel', 'stylesheet')
                .attr('href', 'https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/css/select2.min.css')
                .appendTo('head');
        }

        // Load Select2 JS
        if (!$.fn.select2) {
            $.getScript('https://cdnjs.cloudflare.com/ajax/libs/select2/4.0.13/js/select2.min.js')
                .done(function() {
                    setTimeout(initRemixIconWidget, 100);
                });
        }
    }

    // Initialize when page loads
    loadSelect2();

    // Handle dynamic content (admin inlines)
    $(document).on('formset:added', function(event, $row) {
        setTimeout(initRemixIconWidget, 300);
    });

    // Re-initialize for AJAX content
    const observer = new MutationObserver(function(mutations) {
        let shouldReinit = false;
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === Node.ELEMENT_NODE) {
                        const $node = $(node);
                        if ($node.find('.remix-icon-select[data-widget="remix-icon"]').length > 0) {
                            shouldReinit = true;
                        }
                    }
                });
            }
        });

        if (shouldReinit) {
            setTimeout(initRemixIconWidget, 300);
        }
    });

    // Only observe if document.body exists
    if (document.body) {
        try {
            observer.observe(document.body, {
                childList: true,
                subtree: true
            });
        } catch (error) {
            console.warn('Django Remix Icon: Could not initialize MutationObserver:', error);
        }
    }

})(window.jQuery || window.django.jQuery);
