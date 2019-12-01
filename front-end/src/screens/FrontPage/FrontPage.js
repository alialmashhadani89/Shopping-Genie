import React from "react";
import styled from "@emotion/styled";
import { useState, useEffect } from "react";
import SearchBar from "../../components/SearchBar";
import logo from "../../images/logo15.png";
import { useHistory } from "react-router-dom";

import BackgroundSlider from 'react-background-slider';

import main_image1 from '../../images/main_image1.jpg';
import main_image3 from '../../images/main_image3.png';
import main_image8 from '../../images/main_image8.jpg';
import main_image4 from '../../images/main_image4.jpg';
import main_image10 from '../../images/main_image10.jpg';



const View = styled.div({
  display: "flex"
});

const MainContainer = styled(View)({
  flex: 1,
  justifyContent: "flex-start",
  alignItems: "stretch",
  flexDirection: "column",
  overflowX: "hidden",
  overflowY: "hidden",
  backgroundSize: "cover",
  overflow: "hidden",
  backgroundRepeat: "no-repeat",
  backgroundPosition: "center"
});

const NavBar = styled(View)({
  height: 100,
  flexDirection: "row",
  alignItems: "center",
  marginTop: "10px"
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
  color: "white"
}));

const LogoImage = styled.img({
  width: 300,
  height: 135,
  marginTop: 5
});

const Content = styled(View)({
  flex: 1,
  alignItems: "stretch",
  flexDirection: "column",
  justifyContent: "flex-start"
});

const SearchBarContainer = styled(View)({
  height: 50,
  top: 20,
  marginTop: 130,
  justifyContent: "center"
});

const FrontPage = () => {
  const history = useHistory();
  const [search, setSearch] = useState("");

  const getResults = async term => {
    const splittedSearhc = term.trim();
    if (splittedSearhc.split(" ").length < 2)
      alert("Please enter more than one keyword.");
    else {
      await fetch(`/api/search?search=${term}`);
      history.push("/details", { term });
    }
  };

  const onSubmit = e => {
    e.preventDefault();
    getResults(search);
  };

  return (
    <MainContainer>
     <BackgroundSlider
          images={[main_image1, main_image3, main_image8, main_image4, main_image10]}
          duration={3}
          transition={0.1}
        />
      <NavBar>
        <NavBarImageContainer>
          <RouteItem href="/home" style={{ backgroundColor: "transparent" }}>
            <LogoImage src={logo} />
          </RouteItem>
        </NavBarImageContainer>
        <RoutesContainer>
          <RouteItem selected href="/home">
            Home
          </RouteItem>
          <RouteItem href="/details">Details</RouteItem>
          <RouteItem href="/about">About</RouteItem>
          <RouteItem href="/feedback">FeedBack</RouteItem>
          <RouteItem href="/contact">Contact</RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <SearchBarContainer>
          <SearchBar
            value={search}
            onSubmit={onSubmit}
            onChange={setSearch}
            placeholder="Search Shopping Genie to save time and money..."
          />
        </SearchBarContainer>
      </Content>
    </MainContainer>
  );
};

export default FrontPage;
