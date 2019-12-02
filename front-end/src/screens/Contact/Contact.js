import React from "react";
import styled from "@emotion/styled";
import logo from "../../images/logo15.png";
import backgroundpic from "../../images/contact1.jpg";

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

const Image = styled.img({
  width: 1300,
  height: 450,
  marginLeft: 20,
  marginTop: 25
});

const Text = styled.text({
  marginLeft: 20
});

const ContactPage = () => {
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
          <RouteItem href="/details">Details</RouteItem>
          <RouteItem href="/about"> About</RouteItem>
          <RouteItem href="/feedback">FeedBack</RouteItem>
          <RouteItem selected href="/contact">
            Contact
          </RouteItem>
        </RoutesContainer>
      </NavBar>
      <Content>
        <Text>
          <h2 style={{ marginLeft: "280px", marginTop: "450px", color: "white" }}>
            How Can We Help You?
          </h2>
          <h4 style={{ marginLeft: "280px", color: "white" }}>
            Please contact us, if you have any questions.
            <p>Call-US: 888-888-8888</p>
            <p>Email: pricegenie0499@gmail.com</p>
          </h4>
        </Text>
      </Content>
    </MainContainer>
  );
};
export default ContactPage;
