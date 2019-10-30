import React from "react";
import styled from "@emotion/styled";
import ContctUsBanner from "../../images/contact-us-banner.jpg";
import logo from "../../images/logo13.png";
import backgoundpic from "../../images/111.png";

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

const LogoImage = styled.img({
  width: 250,
  height: 130,
  marginTop: 30
});

const Image = styled.img({
  width: 1300,
  height: 450,
  marginLeft: 20,
  marginTop: 40
});

const Text = styled.text({
  marginLeft: 20,
  color: "white"
});

const ContactPage = () => {
  return (
    <MainContainer>
      <NavBar>
        <NavBarImageContainer>
          <LogoImage src={logo} />
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
        <image>
          <Image src={ContctUsBanner} />
        </image>
        <Text>
          <h2>How can we help you?</h2>
          <h4>Please contact us, if you have any questions.</h4>
          <h4>Call-US: 888-888-8888</h4>
          <h4>Email: xxxxxx@price_genie.com</h4>
        </Text>
      </Content>
    </MainContainer>
  );
};
export default ContactPage;
