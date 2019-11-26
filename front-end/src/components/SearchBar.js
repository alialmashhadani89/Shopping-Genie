import React from "react";
import styled from "@emotion/styled";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";

const Container = styled.div({
  display: "flex",
  flexDirection: "row"
});

const Form = styled.form();

const Input = styled.input({
  padding: "25px",
  fontSize: "20px",
  float: "left",
  borderRadius: 4,
  borderWidth: 1,
  borderBottomRightRadius: 0,
  borderTopRightRadius: 0,
  backgroundColor: "white",
  backgroundImage: "none",
  borderLeftColor: "rgb(205, 205, 205)",
  borderTopColor: "rgb(205, 205, 205)",
  borderBottomColor: "rgb(205, 205, 205)",
  border: "1px solid #ccc",
  background: "#fff",
  display: "block",
  fontFamily: "Arial",
  fontSize: 20,
  fontWeight: 400,
  outline: "none",
  width: "550px",
  height: "52px",
  margin: "0 auto",
  top: 0, // To avoid top: 100px on index.css
  color: "#555",
  lineHeight: "1.42857143",
  boxShadow: "inset 0 1px 1px rgba(0,0,0,.075)",
  transition: "border-color ease-in-out .15s,box-shadow ease-in-out .15s",
  "&:focus": {
    borderColor: "#66afe9"
  }
});

const ButtonContainer = styled.div({});

const Button = styled.button({
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

const Icon = styled.i({
  fontSize: 20,
  content: "\\e003",
  "&::before": {
    content: "\\e003"
  }
});

const SearchBar = ({
  onSubmit,
  onChange,
  value,
  placeholder,
  ...otherProps
}) => {
  return (
    <Form onSubmit={onSubmit} {...otherProps}>
      <Container>
        <Input
          type="text"
          value={value}
          onChange={e => onChange(e.target.value)}
          placeholder={placeholder}
        />
        <ButtonContainer>
          <Button type="submit">
            <FontAwesomeIcon icon={faSearch} />
          </Button>
        </ButtonContainer>
      </Container>
    </Form>
  );
};

export default SearchBar;
