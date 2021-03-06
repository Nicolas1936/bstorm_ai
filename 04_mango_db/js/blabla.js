
// Select the database to use
var db = db.getSiblingDB('DayThree');

var books = db.books;
var editors = db.editors;
var authors = db.authors;

// Erase the database
books.drop();
editors.drop();
authors.drop();

if (!authors.validate().valid) {
    // Authors : firstname, lastname, birthdate, books
    db.createCollection("authors", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                description: "Authors description",
                required: ["firstname", "lastname"],
                properties: {
                    firstname: {
                        bsonType: "string",
                        description: ""
                    },
                    lastname: {
                        bsonType: "string",
                        description: ""
                    },
                    birthdate: {
                        bsonType: "date",
                        description: ""
                    },
                    books: {
                        bsonType: "array",
                        items: {
                            bsonType: "objectId",
                            description: ""
                        }
                    }
                }
            }
        }
    })
    print('Create Authors validator...');
} else {
    print('Authors validator already exist...');
}

if (!editors.validate().valid) {
    //Editors : nbrTVA, name, creationDate, books
    db.createCollection("editors", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                description: "Editors description",
                required: ["nbrTVA", "name"],
                properties: {
                    nbrTVA: {
                        bsonType: "string",
                        description: ""
                    },
                    name: {
                        bsonType: "string",
                        description: ""
                    },
                    creationDate: {
                        bsonType: "date",
                        description: ""
                    },
                    books: {
                        bsonType: "array",
                        items: {
                            bsonType: "objectId",
                            description: ""
                        }
                    }
                }
            }
        }
    }) 
    print('Create Editors validator...');
} else {
    print('Authors validator already exist...');
}

if (!books.validate().valid) {
    // isbn, title, releaseDate, authors, editor
    db.createCollection("books", {
        validator: {
            $jsonSchema: {
                bsonType: "object",
                description: "Books description",
                required: ["isbn", "title"],
                properties: {
                    isbn: {
                        bsonType: "string",
                        description: ""  
                    },
                    title: {
                        bsonType: "string",
                        description: "titre du livre",
                    },
                    releaseDate: {
                        bsonType: "date",
                        description: ""
                    },
                    authors: {
                        bsonType: "array",
                        items: {
                            bsonType: "objectId",
                            description: ""
                        }
                    },
                    editor: {
                        bsonType: "objectId",
                        description: ""
                    }
                }
            }
        }
    })
    print('Create Books validator...');
} else {
    print('Books validator already exist...');
}

//insert all values

//insert values from authors
authors.insertMany([
        // months are 0 indexed !!! jan = 0, feb = 1, ... dec = 11
        { firstname: "John Ronald Reuel", lastname: "Tolkien", birthdate: new Date(1892, 0, 3), books: [] },
        { firstname: "Bertrand", lastname: "Russell", birthdate: new Date(1872, 4, 18), books: [] },
        { firstname: "John", lastname: "Nunn", birthdate: new Date(1955, 3, 18), books: [] },
        { firstname: "Lazlo", lastname: "Polgar", birthdate: new Date(1946, 4, 11), books: [] }
]);
print('Insert Authors in the DB without Books...')

// insert values from editors
editors.insertMany([
        { nbrTVA: "abc123", name: "Harper Collins", creationDate: new Date(), books: [] },
        { nbrTVA: "abc124", name: "Black Dog & Leventhal", creationDate: new Date(), books: [] },
        { nbrTVA: "abc125", name: "GAMBIT", creationDate: new Date(), books: [] },
        { nbrTVA: "abc127", name: "Les Belles Lettres", creationDate: new Date(), books: [] }
]);
print('Insert Editors in the DB without Books...')

// get values of authors and editors

// get values of authors
var tolkien = db.authors.findOne({lastname: "Tolkien"});
var russell = db.authors.findOne({lastname: "Russell"});
var nunn = db.authors.findOne({lastname: "Nunn"});
var polgar = db.authors.findOne({lastname: "Polgar"});
print('Get Authors from DB with new ID');

// get values of editors
var harpercollins = db.editors.findOne({name: "Harper Collins"});
var bdl = db.editors.findOne({name: "Black Dog & Leventhal"});
var gambit = db.editors.findOne({name: "GAMBIT"});
var lbl = db.editors.findOne({name: "Les Belles Lettres"});
print('Get Editors from DB with new ID');

// insert values from books
books.insertMany([
    { isbn: "123456", title: "Lord of the Ring", releaseDate: new Date(), authors: [ tolkien._id ], editor: harpercollins._id },
    { isbn: "456789", title: "The Silmarillion", releaseDate: new Date(), authors: [ tolkien._id ], editor: harpercollins._id },
    { isbn: "123789", title: "Beren and Luthien", releaseDate: new Date(), authors: [ tolkien._id ], editor: harpercollins._id },
    { isbn: "789456", title: "Chess 5334 problems, combination, and games", releaseDate: new Date(), authors: [ polgar._id ], editor: bdl._id },
    { isbn: "456123", title: "John Nunn's chess puzzle book", releaseDate: new Date(), authors: [ nunn._id ], editor: gambit._id },
    { isbn: "654321", title: "Histoire de la philisophie occidentale", releaseDate: new Date(), authors: [ russell._id ], editor: lbl._id }
]);
print('Insert Books in the DB without Authors and Editor...')

// get values of books
var lordofthering = db.books.findOne({isbn: "123456"});
var thesilmarillion = db.books.findOne({isbn: "456789"});
var bal = db.books.findOne({isbn: "123789"});
var chess = db.books.findOne({isbn: "789456"});
var john = db.books.findOne({isbn: "456123"});
var histoire = db.books.findOne({isbn: "654321"});
print('Get Books from DB with new ID');

// insert books into authors
tolkien.books.push(
                    lordofthering._id, 
                    thesilmarillion._id, 
                    bal._id
);
polgar.books.push(chess._id);
nunn.books.push(john._id);
russell.books.push(histoire._id);
print('Add Books inside the Authors')

// insert books into editors
harpercollins.books.push(
                            lordofthering._id, 
                            thesilmarillion._id, 
                            bal._id
);
bdl.books.push(chess._id);
gambit.books.push(john._id);
lbl.books.push(histoire._id);
print('Add Books inside the Editors')

// insert authors in the DB
authors.updateOne({_id: tolkien._id}, {$set: tolkien});
authors.updateOne({_id: russell._id}, {$set: russell});
authors.updateOne({_id: nunn._id}, {$set: nunn});
authors.updateOne({_id: polgar._id}, {$set: polgar});
print('Insert Authors in the DB with Books...')

// insert editors in the DB
editors.updateOne({_id: harpercollins._id}, {$set: harpercollins});
editors.updateOne({_id: bdl._id}, {$set: bdl});
editors.updateOne({_id: gambit._id}, {$set: gambit});
editors.updateOne({_id: lbl._id}, {$set: lbl});
print('Insert Editors in the DB with Books...')

// insert books in the Db
books.updateOne({_id: lordofthering._id}, {$set: lordofthering});
books.updateOne({_id: thesilmarillion._id}, {$set: thesilmarillion});
books.updateOne({_id: bal._id}, {$set: bal});
books.updateOne({_id: chess._id}, {$set: chess});
books.updateOne({_id: john._id}, {$set: john});
books.updateOne({_id: histoire._id}, {$set: histoire});
print('Insert Books in the DB with Authors and Editor...')


