import { json, useLoaderData } from "@remix-run/react";

const findAllWitches = async () => {
  return [
    { id: 1, name: "Hermione Granger" },
    { id: 2, name: "Willow Rosenberg" },
  ]
}

export const loader = async () => {
  const witches = await findAllWitches();
  return json({ witches });
}

export default function Index() {
  const { witches } = useLoaderData<typeof loader>();
  return (
    <>
      {witches.map((witch) => (
        <div key={witch.id}>{witch.name}</div>
      ))}
    </>
  )
}
