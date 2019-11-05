import React from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo15.png";
//import aboutbanner from "../../images/about-banner2.png";
import grouppic from "../../images/group-pic.png";
import sallypic from "../../images/sally.jpg";
import stevenpic from "../../images/steven.jpg";
import alipic from "../../images/ali.jpg";
import backgroundpic from "../../images/about5.jpg";

//import React, { component } from 'react'
//import HorizontalScroll from 'react-scroll-horizontal'

const View = styled.div({
  display: "flex"
});

const Content = styled(View)({
  flex: 1,
  alignItems: "stretch",
  flexDirection: "column",
  justifyContent: "flex-start"
});

const MainContainer = styled(View)({
  flex: 1,
  justifyContent: "flex-start",
  alignItems: "stretch",
  flexDirection: "column",
  backgroundImage: `url(${backgroundpic})`,
  backgroundSize: "cover",
  overflow: "hidden",
  backgroundRepeat: "no-repeat",
  backgroundPosition: "center"
});

const NavBar = styled(View)({
  height: 150,
  flexDirection: "row",
  alignItems: "center"
});

const NavBarImageContainer = styled(View)({
  marginLeft: 20
});

const RoutesContainer = styled(View)({
  flex: 1,
  marginLeft: 20,
  flexDirection: "row",
  justifyContent: "flex-start",
  alignItems: "center"
});

const RouteItem = styled.a(({ selected }) => ({
  padding: "20px 20px",
  //backgroundColor: selected ? "orange" : "transparent",
  color: "black",
  //"&:hover": {
    //backgroundColor: selected ? "orange" : "lightgrey",
    //color: selected ? "white" : "green"
  //}
}));

const Image = styled.img({
  width: 500,
  height: 400,
  float: "left",
  marginLeft: 50
});
const Image2 = styled.img({
  width: 500,
  height: 400,
  float: "right",
  marginRight: 70
});

const ImageAli = styled.img({
  width: 300,
  height: 400,
  float: "left",
  marginLeft: 50,
  marginTop: 30
});

const ImageSteven = styled.img({
  width: 300,
  height: 400,
  float: "center",
  marginTop: 40,
  marginLeft: 180
});

const ImageSally = styled.img({
  width: 300,
  height: 400,
  float: "right",
  marginTop: 40,
  marginRight: 150
});

const TextAli = styled.text({
  float: "left",
  marginLeft: 50
});

const TextSteven = styled.text({
  float: "left",
  marginLeft: 80
});

const TextSally = styled.text({
  float: "right",
  marginRight: 120
});

const LogoImage = styled.img({
  width: 300,
  height: 135,
  marginTop: 5
});

const AboutPage = () => {
  return (
    <MainContainer style={{ width: "800px", height: "1400px"}}>
      <NavBar>
        <NavBarImageContainer>
          <RouteItem href="/home">
            <LogoImage src={logo} />
          </RouteItem>
        </NavBarImageContainer>
        <RoutesContainer>
          <RouteItem href="/home">Home</RouteItem>
          <RouteItem href="/details">Details</RouteItem>
          <RouteItem selected href="/about">
            About
          </RouteItem>
          <RouteItem href="/feedback">FeedBack</RouteItem>
          <RouteItem href="/contact">Contact</RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <text style={{ marginLeft: 50, marginTop: 40, color: "black" }}>
          <h2>
            <b> Who We Are? </b>
          </h2>
          <h3> We are developers, problem-solvers, and challengers!</h3>
        </text>


        <image>
          <Image src={grouppic} style={{ marginTop: 25 }} />
        </image>

        <text style={{marginLeft: "780px", marginTop: "-480px", color: "black"}}>
        <h3> We are dreamers, and we desire to have a positive impact
        <p> on peoples lives through computers. </p>
        </h3>
        </text>


        <image>
          <ImageAli src={alipic} style={{marginTop:"450px"}} />
          <ImageSteven src={stevenpic} style={{marginTop: "450px"}}/>
          <ImageSally src={sallypic} style={{marginTop: "450px"}} />
        </image>
        <text style={{color:"black"}}>
          <TextAli>
            <b>
              <h2>Ali Almashhadani</h2>
              <h3>[Back-End Developer & AI,Database]</h3>
            </b>
          </TextAli>
          <TextSteven>
            <b>
              <h2>Steven Santana</h2>
              <h3>[Back-End Developer & Database]</h3>
            </b>
          </TextSteven>
          <TextSally>
            <b>
              <h2>Sally Xuan</h2>
              <h3>[Front-End Developer & Design]</h3>
            </b>
          </TextSally>
        </text>
      </Content>
    </MainContainer>
  );
};
export default AboutPage;
