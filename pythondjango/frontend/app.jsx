const App = () => {
  const chais = window.chais || [];
  console.log(chais, 'taha')
  return (
    <div>
      <h1>Chais</h1>
      {chais.map((c, i) => (
        <p key={i}>
          {c.name} - {c.age}
        </p>
      ))}
    </div>
  );
};

export default App;
