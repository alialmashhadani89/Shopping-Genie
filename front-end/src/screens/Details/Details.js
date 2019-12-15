import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import styled from "@emotion/styled";
import moment from "moment-timezone";
import { useHistory } from "react-router-dom";
import backgroundpic from "../../images/detail.jpg";
import logo from "../../images/logo15.png";
import SearchBar from "../../components/SearchBar";
import bestbuylogo from "../../images/bb.png";
import bhlogo from "../../images/bh.png";
import amazonlogo from "../../images/aa.png";
import walmartlogo from "../../images/wm.png";
import MDSpinner from "react-md-spinner";
import noResultImag2 from "../../images/no_result_found.gif";

const View = styled.div({
  display: "flex"
});

const MainContainer = styled(View)({
  flex: 1,
  justifyContent: "flex-start",
  alignItems: "stretch",
  flexDirection: "column",
  overflowX: "hidden",
  backgroundImage: `url(${backgroundpic})`,
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
  //backgroundColor: "grey",
  flex: 1,
  marginLeft: 20,
  flexDirection: "row",
  justifyContent: "flex-start",
  alignItems: "center"
});

const RouteItem = styled.a(({ selected }) => ({
  padding: "20px 20px",
  //backgroundColor: selected ? "orange" : "transparent",
  color: "black"
  //"&:hover": {
  //  backgroundColor: selected ? "orange" : "lightgrey",
  // color: selected ? "white" : "green"
  //}
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
    backgroundColor: "#dda"
  },
  "& th, & td": {
    backgroundColor: "#ddd",
    border: "4px solid #000",
    padding: 15
  },
  "& th": {
    textAlign: "center",
    paddingTop: 20,
    paddingBottom: 20,
    backgroundColor: "#ffad99",
    color: "black"
  }
});

const LinkButton = styled.button({
  backgroundColor: "#cc2900",
  width: "100px",
  padding: "12.5px",
  height: "52px",
  color: "white",
  borderTopLeftRadius: 0,
  borderBottomLeftRadius: 0,
  borderTopRightRadius: 4,
  borderBottomRightRadius: 4,

  "&:hover": {
    backgroundColor: "#f4511e"
  }
});

const TableBody = styled.tbody({});

const ResultsImage = styled.img({
  height: 50
});

function checkSpin(results) {
  if (results.length == 0) {
    return true;
  } else {
    return false;
  }
}

function checklogo(storeName) {
  if (storeName.trim() == "B&H") {
    return bhlogo;
  } else if (storeName.trim() == "Amazon") {
    return amazonlogo;
  } else if (storeName.trim() == "Best Buy") {
    return bestbuylogo;
  } else {
    return walmartlogo;
  }
}

const onClick = storeLink => {
  var win = window.open(storeLink, "_blank");
  win.focus();
  return false;
};

const RenderItem = ({
  image,
  brand,
  itemName,
  itemPrice,
  predictionPrice,
  predictionDate,
  storeName,
  storeLink
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
    <td>
      <LinkButton id="bt" onClick={() => onClick(storeLink)}>
        Take me
      </LinkButton>
    </td>
  </tr>
);

const Details = () => {
  const {
    location: { state }
  } = useHistory();
  const [search, setSearch] = useState((state && state.term) || "");
  const [results, setResults] = useState([]);
  const [noResults, setNoResults] = useState(false);

  const getResults = term => {
    setNoResults(false);
    fetch(`/api/results?search=${term}`)
      .then(res => res.json())
      .then(res => {
        if (Array.isArray(res) && res.length > 0) setResults(res);
        else {
          setResults([]);
          setNoResults(true);
        }
      });
  };

  const onSubmit = e => {
    e.preventDefault();
    getResults(search);
    setResults([]);
  };

  useEffect(() => {
    getResults(search);
  }, []);

  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <RouteItem href="/home">
            <LogoImage src={logo} />
          </RouteItem>
        </NavBarImageContainer>
        <RoutesContainer>
          <RouteItem href="/home">Home</RouteItem>
          <RouteItem selected href="/details">
            Details
          </RouteItem>
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
        <ResultsContainer>
            {checkSpin(results) && !noResults && (
              <MDSpinner
                size={50}
                style={{
                  marginTop: "50px",
                  marginLeft: "0px"
                }}
              />
            )}
            {!checkSpin(results) && (
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
                    <h5> Store </h5>
                  </th>
                  <th>
                    <h5> Link </h5>
                  </th>
                </tr>
              </thead>
              
              <TableBody>
                {" "}
                {results.map(item => (
                  <RenderItem key={item.id} {...item} />
                ))}
              </TableBody>
            
              </Table>)}
            {noResults && (
              <img src={noResultImag2} style={{height:"350px"}} />
            )}
        </ResultsContainer>
      </Content>
    </MainContainer>
  );
};

export default Details;
