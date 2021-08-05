import gulp from "gulp";
import gulpSass from "gulp-sass";
import nodeSass from "node-sass";
import postcss from "gulp-postcss";
import csso from "gulp-csso";
import tailwindcss from "tailwindcss";
import autoprefixer from "autoprefixer";
import del from "del";
import babelify from "babelify";
import bro from "gulp-bro";

const sass = gulpSass(nodeSass);

const paths = {
  scss: {
    src: "assets/scss/styles.scss",
    dest: "static/css",
    watch: "assets/scss/**/*.scss",
  },
  js: {
    src: "assets/js/main.js",
    dest: "static/js",
    watch: "assets/js/**/*.js",
  },
};

const styles = () => {
  return gulp
    .src(paths.scss.src)
    .pipe(sass().on("error", sass.logError))
    .pipe(postcss([tailwindcss, autoprefixer]))
    .pipe(csso())
    .pipe(gulp.dest(paths.scss.dest));
};

const js = () =>
  gulp
    .src(paths.js.src)
    .pipe(
      bro({
        transform: [babelify.configure({ presets: ["@babel/preset-env"] })],
      })
    )
    .pipe(gulp.dest(paths.js.dest));

const watch = () => {
  gulp.watch(paths.scss.watch, styles);
  gulp.watch(paths.js.watch, js);
};

const clean = () => del(["static/css/"]);
const assets = gulp.series([styles, js]);

export const build = gulp.series([clean, assets]);
export const dev = gulp.series([build, watch]);
