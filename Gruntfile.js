/* global module */

module.exports = function (grunt) {
	grunt.initConfig({
		bowercopy: {
			options: {
				srcPrefix: 'bower_components'
			},

			libs: {
				options: {
					destPrefix: 'static/js/libs'
				},
				files: {
					'fastclick.js': 'foundation/js/vendor/fastclick.js',
					'jquery.cookie.js': 'foundation/js/vendor/jquery.cookie.js',
					'jquery.js': 'foundation/js/vendor/jquery.js',
					'modernizr.js': 'foundation/js/vendor/modernizr.js',
					'placeholder.js': 'foundation/js/vendor/placeholder.js',
					'foundation.min.js': 'foundation/js/foundation.min.js'
				}
			},

			css: {
				options: {
					destPrefix: 'static/css'
				},
				files: {
					'foundation.css': 'foundation/css/foundation.css',
					'normalize.css': 'foundation/css/normalize.css',
					'font-awesome.min.css': 'font-awesome/css/font-awesome.min.css'
				}
			},

			fonts: {
				options: {
					destPrefix: 'static/fonts'
				},
				files: {
					'fontawesome-webfont.eot': 'font-awesome/fonts/fontawesome-webfont.eot',
					'fontawesome-webfont.svg': 'font-awesome/fonts/fontawesome-webfont.svg',
					'fontawesome-webfont.ttf': 'font-awesome/fonts/fontawesome-webfont.ttf',
					'fontawesome-webfont.woff': 'font-awesome/fonts/fontawesome-webfont.woff'
				}
			}
		}
	});

	grunt.loadNpmTasks('grunt-bowercopy');

	grunt.registerTask('default', ['bowercopy']);
};