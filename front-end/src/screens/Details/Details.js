import React, { useState, useEffect } from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo2.png";
import SearchBar from "../../components/SearchBar";
// import "./Details.css";

const View = styled.div({
  display: "flex"
});

const MainContainer = styled(View)({
  flex: 1,
  backgroundColor: "aquamarine",
  justifyContent: "flex-start",
  alignItems: "stretch",
  flexDirection: "column"
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
  width: 100,
  height: 100
});

const Content = styled(View)({
  flex: 1,
  alignItems: "stretch",
  flexDirection: "column",
  justifyContent: "flex-start"
});

const SearchBarContainer = styled(View)({
  height: 50,
  marginTop: 100,
  justifyContent: "center"
});

const ResultsContainer = styled(View)({
  flex: 1,
  marginTop: 30,
  alignItems: "center",
  justifyContent: "center"
});

const Table = styled.table({
  flex: 1,
  marginLeft: 30,
  marginRight: 30
});

const RenderItem = ({ image, price, name, model, logo }) => (
  <tr>
    <td>{image} </td>
    <td>{price} </td>
    <td>{name} </td>
    <td>{model} </td>
    <td>{logo} </td>
  </tr>
);

const Details = () => {
  const [results, setResults] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/results")
      .then(res => res.json())
      .then(res => {
        if (Array.isArray(res)) setResults(res);
      });
  }, []);
  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <Image src={logo} />
        </NavBarImageContainer>
        <RoutesContainer>
          <RouteItem href="/home">Home</RouteItem>
          <RouteItem selected href="/details">
            Details
          </RouteItem>
          <RouteItem href="/about">About</RouteItem>
          <RouteItem href="/feedback">Feedback</RouteItem>
          <RouteItem href="/contact">Contact</RouteItem>
        </RoutesContainer>
      </NavBar>

      <Content>
        <SearchBarContainer>
          <SearchBar />
        </SearchBarContainer>
        <ResultsContainer>
          <Table id="products">
            <thead>
              <tr>
                <th>
                  {" "}
                  <h4> Product Picture </h4>{" "}
                </th>
                <th>
                  {" "}
                  <h4> Price Detail </h4>{" "}
                </th>
                <th>
                  {" "}
                  <h4> Product Name </h4>{" "}
                </th>
                <th>
                  {" "}
                  <h4> Prediction Model </h4>{" "}
                </th>
                <th>
                  {" "}
                  <h4> Store Logo </h4>{" "}
                </th>
              </tr>
            </thead>
            <tbody>
              {results.map(item => (
                <RenderItem key={item.id} {...item} />
              ))}
            </tbody>
          </Table>
        </ResultsContainer>
      </Content>
    </MainContainer>
  );
};

export default Details;
