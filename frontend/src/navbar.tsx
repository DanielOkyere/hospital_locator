import React from 'react';

interface NavbarProps {
    username: string;
}

const Navbar: React.FC<NavbarProps> = ({ username }) => {
    return (
        <nav className="bg-gray-800">
      <div className="max-w-4xl mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          <div className="flex-shrink-0">
            <a href="#" className="text-white font-bold text-lg">HLC</a>
          </div>
          <div className="flex space-x-4">
            <a href="#" className="text-gray-300 hover:text-white">Home</a>
            <a href="#" className="text-gray-300 hover:text-white">Profile ({username})</a>
            <a href="#" className="text-gray-300 hover:text-white">Logout</a>
          </div>
        </div>
      </div>
    </nav>
    );
};

export default Navbar;
