import React from "react";
import styled from "@emotion/styled";

const Container = styled.div({
  display: "flex",
  flexDirection: "row"
});

const Form = styled.form();

const Input = styled.input({
  padding: "25px",
  fontSize: "20px",
  background: "rgba(255, 255, 255, 0.4)",
  border: "none",
  display: "block",
  outline: "none",
  width: "300px",
  height: "50px",
  margin: "0 auto",
  top: 0, // To avoid top: 100px on index.css
  color: "#333",
  WebkitBoxShadow: "0 2px 10px 1px rgba(0, 0, 0, 0.5)",
  boxShadow: "0 2px 10px 1px rgba(0, 0, 0, 0.5)"
});

const ButtonContainer = styled.div({});

const Button = styled.button({
  backgroundColor: "orange",
  width: "100px",
  padding: "12.5px",
  height: "52px"
});

const Icon = styled.i({
  fontSize: 20
});

const SearchBar = ({ onSubmit, ...otherProps }) => {
  return (
    <Form onSubmit={onSubmit} {...otherProps}>
      <Container>
        <Input />
        <ButtonContainer>
          <Button className="btn-control" type="submit" />
          <Icon className="glyphicon"></Icon>
        </ButtonContainer>
      </Container>
    </Form>
  );
};

export default SearchBar;
