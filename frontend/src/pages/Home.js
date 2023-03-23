import React from "react";

import About from "../components/About";
import Contact from "../components/Contact";
import Hero from "../components/Hero";
import Projects from "../components/Projects";
import Technologies from "../components/Technologies";
import Certifications from "../components/Certifications";

const Home = () => {
  return (
    <div id="home">
      <Hero />
      <About />
      <Projects />
      <Technologies />
      <Certifications />
      <Contact />
    </div>
  );
};

export default Home;