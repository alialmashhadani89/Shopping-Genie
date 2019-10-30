import React from "react";
import styled from "@emotion/styled";
import { useState, useEffect } from "react";
import SearchBar from "../../components/SearchBar";
import logo from "../../images/logo13.png";
import { useHistory } from "react-router-dom";
import backgoundpic from "../../images/paralax.jpg";

async function submitForm(e, history) {
  e.preventDefault();
  const searchInput = document.getElementById("search-term");
  const searchValue = searchInput.value;
  const new_searchValue = searchValue.trim();
  if (new_searchValue.split(" ").length < 2)
    alert("Please enter more than one keyword.");
  else {
    const results = await fetch(`/api/search?search=${searchValue}`);

    history.push("/details");
  }
}

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
  backgroundImage: `url(${backgoundpic})`,
  backgroundSize: "cover",
  overflow: "hidden",
  backgroundRepeat: "no-repeat",
  backgroundPosition: "center"
});

const NavBar = styled(View)({
  height: 100,
  flexDirection: "row",
  alignItems: "center"
});

const NavBarImageContainer = styled(View)({
  marginLeft: 20
});

const RoutesContainer = styled(View)({
  backgroundColor: "grey",
  flex: 1,
  marginLeft: 20,
  flexDirection: "row",
  justifyContent: "flex-start",
  alignItems: "center"
});

const RouteItem = styled.a(({ selected }) => ({
  padding: "15px 15px",
  backgroundColor: selected ? "orange" : "transparent",
  color: "white",
  "&:hover": {
    backgroundColor: selected ? "orange" : "lightgrey",
    color: selected ? "white" : "green"
  }
}));

const Image = styled.img({
  width: 250,
  height: 130,
  marginTop: 30
});

const Content = styled(View)({
  flex: 1,
  alignItems: "stretch",
  flexDirection: "column",
  justifyContent: "flex-start"
});

const SearchBarContainer = styled(View)({
  height: 50,
  top: 100,
  marginTop: 250,
  justifyContent: "center"
});

const FrontPage = () => {
  const history = useHistory();
  const [search, setSearch] = useState("");
  const [results, setResults] = useState([]);

  const getResults = term => {
    fetch(`/api/results?search=${search}`)
      .then(res => res.json())
      .then(res => {
        if (Array.isArray(res)) setResults(res);
      });
  };

  const onSubmit = e => {
    e.preventDefault();
    getResults(search);
  };

  useEffect(() => {
    getResults(search);
  }, []);

  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <Image src={logo} />
        </NavBarImageContainer>
        <RoutesContainer>
          <RouteItem selected href="/home">
            Home
          </RouteItem>
          <RouteItem href="/details">Details</RouteItem>
          <RouteItem href="/about">About</RouteItem>
          <RouteItem href="/feedback">Feedback</RouteItem>
          <RouteItem href="/contact">Contact</RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <SearchBarContainer>
          <SearchBar
            value={search}
            onSubmit={onSubmit}
            onChange={setSearch}
            placeholder="Search Price Genie to save your time and money..."
          />
        </SearchBarContainer>
      </Content>
    </MainContainer>
  );
};

export default FrontPage;
