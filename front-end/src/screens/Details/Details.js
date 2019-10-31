import React, { useState, useEffect } from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo13.png";
import SearchBar from "../../components/SearchBar";
import moment from "moment-timezone";
import bestbuylogo from "../../images/bb.png";
import bhlogo from "../../images/bh.png";
import amazonlogo from "../../images/aa.png";
import walmartlogo from "../../images/wm.png";

const View = styled.div({
  display: "flex"
});

const MainContainer = styled(View)({
  flex: 1,
  justifyContent: "flex-start",
  alignItems: "stretch",
  flexDirection: "column",
  overflowX: "hidden"
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

const LogoImage = styled.img({
  width: 250,
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
  marginTop: 20,
  justifyContent: "center"
});

const ResultsContainer = styled(View)({
  flex: 1,
  marginTop: 30,
  alignItems: "stretch",
  justifyContent: "center"
});

const Table = styled.table({
  borderCollapse: "collapse",
  display: "block",
  borderColor: "#000",
  "& *": {
    boxSizing: "border-box"
  },
  "& th:hover": {
    backgroundColor: "#ddd"
  },
  "& th, & td": {
    border: "4px solid #ddd",
    padding: 15
  },
  "& th": {
    textAlign: "center",
    paddingTop: 20,
    paddingBottom: 20,
    backgroundColor: "dodgerblue",
    color: "white"
  }
});

const TableBody = styled.tbody({});

const ResultsImage = styled.img({
  height: 50
});

function checklogo(storeName) {
  if (storeName.trim() == "B&H") {
    return bhlogo;
  } else {
    return bestbuylogo;
  }
}

const RenderItem = ({
  image,
  brand,
  itemName,
  itemPrice,
  predictionPrice,
  predictionDate,
  storeName
}) => (
  <tr>
    <td>
      <ResultsImage src={image} />
    </td>
    <td>{brand} </td>
    <td>{itemName} </td>
    <td>{itemPrice} </td>
    <td>{predictionPrice} </td>
    <td>{moment(predictionDate).format("MM/YYYY")} </td>
    <td>
      <ResultsImage src={checklogo(storeName)} />
    </td>
    <td>{storeName} </td>
  </tr>
);

const Details = () => {
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
          <RouteItem href="/home" style={{ backgroundColor: "white" }}>
            <LogoImage src={logo} />
          </RouteItem>
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
          <SearchBar
            value={search}
            onSubmit={onSubmit}
            onChange={setSearch}
            placeholder="Search Price Genie to save your time and money..."
          />
        </SearchBarContainer>
        <ResultsContainer>
          <Table id="products">
            <thead>
              <tr>
                <th>
                  <h5> Item Image </h5>
                </th>
                <th>
                  <h5> Product Brand </h5>
                </th>
                <th>
                  <h5> Product Name </h5>
                </th>
                <th>
                  <h5> Price </h5>
                </th>
                <th>
                  <h5> Prediction Price </h5>
                </th>
                <th>
                  <h5> Prediction Date </h5>
                </th>
                <th>
                  <h5> Store Logo </h5>
                </th>
                <th>
                  <h5> Store Name </h5>
                </th>
              </tr>
            </thead>
            <TableBody>
              {results.map(item => (
                <RenderItem key={item.id} {...item} />
              ))}
            </TableBody>
          </Table>
        </ResultsContainer>
      </Content>
    </MainContainer>
  );
};

export default Details;
