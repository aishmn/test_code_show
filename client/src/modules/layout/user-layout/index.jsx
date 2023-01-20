export default function UserLayout({ children }) {
  return (
    <div>
      <nav className="grid grid-cols-2">
        <section>Jobzill</section>
        <section>
          <ul className="grid grid-flow-row bg-neutral-300">
            <li>Home</li>
            <li>Home</li>
            <li>Home</li>
            <li>Home</li>
            <li>Home</li>
          </ul>
        </section>
      </nav>
      {children}
    </div>
  );
}
