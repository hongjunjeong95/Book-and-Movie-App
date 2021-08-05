gsap.to(".show_up_book", {
  scrollTrigger: {
    trigger: ".show_up_book",
    start: "-90% 80%",
    end: "-50% 90%",
    scrub: 1,
  },
  opacity: 1,
  y: 0,
});

gsap.to(".show_up_movie", {
  scrollTrigger: {
    trigger: ".show_up_movie",
    start: "-100% 100%",
    end: "-50% 90%",
    scrub: 1,
  },
  opacity: 1,
  y: 0,
});

gsap.to(".show_up_people", {
  scrollTrigger: {
    trigger: ".show_up_people",
    start: "-100% 100%",
    end: "-50% 90%",
    scrub: 1,
  },
  opacity: 1,
  y: 0,
});
