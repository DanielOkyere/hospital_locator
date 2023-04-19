import React from 'react';

interface SearchFormProps {
  onSearch: (query: string) => void;
}

const SearchForm: React.FC<SearchFormProps> = ({ onSearch }) => {
  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const query = formData.get('query') as string;
    onSearch(query);
  };

  return (
    <form className="absolute top-0 left-0 w-full p-4" onSubmit={handleSubmit}>
      <label htmlFor="query" className="sr-only">Search</label>
      <div className="relative">
        <input
          type="text"
          name="query"
          id="query"
          className="bg-white border border-gray-300 rounded-full py-2 px-4 block w-full appearance-none leading-5 focus:outline-none focus:border-blue-400"
          placeholder="Search for a location"
        />
        <button
          type="submit"
          className="absolute top-0 right-0 mt-2 mr-2"
        >
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 text-gray-500" viewBox="0 0 20 20" fill="currentColor">
            <path fillRule="evenodd" d="M13.885 14.926l4.706 4.706a1 1 0 01-1.414 1.414l-4.706-4.706a8.5 8.5 0 111.414-1.414zM8.5 15.5a7 7 0 100-14 7 7 0 000 14z" clipRule="evenodd" />
          </svg>
        </button>
      </div>
    </form>
  );
};

export default SearchForm;
