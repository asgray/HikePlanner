import React from "react";
import Input from "../input";

const FoodInputs = ({ row, onChange }) => {
  return (
    <>
      <Input
        name="name"
        type="text"
        onChange={onChange}
        label="Name:"
        example="Mac and Cheese"
        value={row["name"]}
      />
      <Input
        name="brand"
        type="text"
        onChange={onChange}
        label="Brand:"
        example="Kraft"
        value={row["brand"]}
      />
      <Input
        name="weight"
        type="number"
        onChange={onChange}
        label="Weight:"
        example="Weight (g) per serving"
        value={row["weight"]}
      />
      <Input
        name="calories"
        type="number"
        onChange={onChange}
        label="Calories:"
        example="Calories per serving"
        value={row["calories"]}
      />
      <Input
        name="protein"
        type="number"
        onChange={onChange}
        label="Protein:"
        example="Protein (g) per serving"
        value={row["protein"]}
      />
      <Input
        name="servings"
        type="number"
        onChange={onChange}
        label="Servings:"
        example="Servings per container"
        value={row["servings"]}
      />
      <Input
        name="cooked"
        type="radio"
        onChange={onChange}
        label="Cooked:"
        example="Yes"
      />
      <Input
        name="cooked"
        type="radio"
        onChange={onChange}
        label=""
        example="No"
      />
    </>
  );
};

export default FoodInputs;
