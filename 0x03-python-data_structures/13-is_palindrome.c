#include "lists.h"
/**
 * RecursivePalindrome - Verific if the linked list is palindrome.
 * @left: Is my reference to the head of my list
 * @right: Is my last element take it in recursion.
 * Return: 0 if not or 1 if yes palindrome
 */
int RecursivePalindrome(listint_t **left, listint_t *right)
{
	int pal;

	if (right == NULL)
		return (1);

	pal = RecursivePalindrome(left, right->next);
	if (pal == 0)
		return (0);

	pal = (right->n == (*left)->n);

	*left = (*left)->next;
	return (pal);
}
/**
 * is_palindrome - Verific if the linked list is palindrome.
 * @head: Give me the list
 * Return: 0 if not or 1 if yes palindrome
 */
int is_palindrome(listint_t **head)
{
	int res;

	if (!head)
		return (0);
	res = RecursivePalindrome(head, *head);
	return (res);
}
